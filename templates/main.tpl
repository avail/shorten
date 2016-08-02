<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <link rel="stylesheet" href="assets/style.css" />
    <script src="//code.jquery.com/jquery-3.1.0.min.js"></script>
    <script src="/assets/magic.js"></script>
</head>
<body>
    <div id="outer-wrapper">
        <div id="inner-wrapper">
            <h1>avail's url shortener</h1>
            {% if errorid != 0 %}
            <small class="error">{{ errors[errorid] }}</small>
            {% end %}

            <form method="POST">
                <label for="url">URL:</label>
                <input type="text" name="url" id="url" placeholder="http://ripple.moe">

                <button type="submit" class="btn btn-success">Submit <span class="fa fa-arrow-right"></span></button>
            </form>

            <br />

            <p>
                CLI usage: send a POST request with your desired URL in the 'url' parameter. Response is the shortened ID.
            </p>

            <br />

            <h3 id="shortened-title"></h3>
            <ul id="shortened">

            </ul>

            <br />
            <a href="https://github.com/avail/shorten">source</a> | <a href="mailto:avail@pomf.se">contact</a>

        </div>
    </div>
</body>
</html>