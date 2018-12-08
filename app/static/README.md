## Replacing few lines in all HTML files

In place of
```
<link href="{{ url_for('static',filename='css/metro-all.min.css') }}" rel="stylesheet">
```
replace with
```
<link rel="stylesheet" href="https://cdn.metroui.org.ua/v4/css/metro-all.min.css">
```
And In place of
```
<script type="text/javascript" src="{{ url_for('static',filename='js/metro.min.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static',filename='js/featurate.js') }}"></script>
```
replace with
```
<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdn.metroui.org.ua/v4/js/metro.min.js"></script>
```
