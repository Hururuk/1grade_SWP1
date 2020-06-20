html = b"""
<html>
    <body>
        <form method="get" action="">
            <p>
                A : <input type="number" name="a">
            </p>
            <p>
                B : <input type="number" name="b">
            </p>
            <p>
            <input type="submit">
        </form>
        <p>
            a + b: %(x)s</br>
            a * b: %(y)s</br>
        </p>
    </body>
</html>
"""
