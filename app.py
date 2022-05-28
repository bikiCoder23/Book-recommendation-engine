from flask import Flask, render_template, request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl', 'rb'))
final_rating_df = pickle.load(open('final_rating_df.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['User-Count'].values),
                           rating=list(popular_df['Avg-Rating'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    book_index = np.where(final_rating_df.index == user_input)[0][0]
    book_list = sorted(list(enumerate(similarity_scores[book_index])), key=lambda x: x[1], reverse=True,)[1:5]

    data = []
    for i in book_list:
        item = []
        temp_df = books[books['Book-Title'] == final_rating_df.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
