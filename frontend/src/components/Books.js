import React from 'react'

function Books() {
    const books = [{name:'firstbook', price:50, pageNumber: 350},{name:'secondBook', price:55, pageNumber: 380}]
    return (
        <div>
            {books.map(book=> <div>
                {book.name}
                {book.price}
                {book.pageNumber}
            </div>)}
        </div>
    )
}

export default Books
