from flask import Flask, request, jsonify, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/wiki/<string:search_term>', methods=['GET'])
def search_wiki(search_term):
    try:
        language = request.args.get('lang', default='cs')

        response = requests.get(f'https://{language}.wikipedia.org/w/api.php',
                                params={'action': 'query',
                                        'list': 'search',
                                        'srsearch': search_term,
                                        'format': 'json'})
        data = response.json()

        if not data['query']['search']:
            return jsonify({'error': 'Article not found'}), 404

        # checkikng first article is the same as the "word"
        first_article_title = data['query']['search'][0]['title']
        if first_article_title.lower() != search_term.lower():
            # If the "word"" isn´t the same, but exist in another article return 303
            search_url = f'https://{language}.wikipedia.org/wiki/Special:Search?search={search_term}'
            return redirect(search_url, code=303)

        # write the first paragraph if the word is teh same as the title
        article_id = data['query']['search'][0]['pageid']
        extract_response = requests.get(f'https://{language}.wikipedia.org/w/api.php',
                                        params={'action': 'query',
                                                'prop': 'extracts',
                                                'pageids': article_id,
                                                'explaintext': 'true',
                                                'format': 'json'})
        extract_data = extract_response.json()
        first_paragraph = extract_data['query']['pages'][str(article_id)]['extract'].split('\n')[0]
        return jsonify({'result': first_paragraph}), 200

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
