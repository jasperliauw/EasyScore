# https://www.youtube.com/watch?v=dam0GPOAvVI&list=LL&index=3&t=7560s
print("Hello World!")

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)