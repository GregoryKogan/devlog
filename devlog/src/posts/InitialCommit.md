## Code Highlighting examples

<br />

1. keyword
```JavaScript
for (const foo of bar) {
        if (foo === 'foobar') break;
        await foo;
}
```

2. builtin
```python
pi = round(float('3.14159'), 2)
```
```Typescript
type SearchFunc = (source: string, subStr: string) => boolean;
```

3. class-name
```JavaScript
class Rectangle extends Square { /* ... */ }
```
```Csharp
public class CameraController : MonoBehaviour { /* ... */ }
```

4. function
```JavaScript
function isEven(number) {
	    return Number(number) % 2 === 0;
}
const isOdd = (number) => !isEven(number);
```

5. boolean
```JavaScript
console.log(true === false); // prints false
console.log(true === !false); // prints true
```

6. number
```Python
print(3.14159 * 42)
print(1e100 + .001j)
return foo & 0xdeadbeef
```

7. string
```JavaScript
let greeting = 'Hello World!';
```

8. char
```Elm
['A', 'z', '0', '-', '\t', '\u{2728}']
```

9. symbol
```Smalltalk
#myFirstSymbol "#myFirstSymbol is a symbol in Smalltalk"
```

10. regex
```JavaScript
let entity = /&#x?[\da-f]{1,8};/;
```

11. url
```css
body {
	    background: url(foo.png);
}
```
```Markdown
[Prism](https://prismjs.com) is a cool syntax highlighter.
```

12. operator
```JavaScript
x += (y + 4 >> -z === w) ? b ** c : ~a;
```

13. variable
```Bash
echo $STRING
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]}
```

14. constant
```JavaScript
const PI = 3.14159;
```
```C
fprintf(stdout, "hello world\n");
```

15. property
```CSS
body {
	    color: red;
	    line-height: normal;
}
```
```JSON
{
        "data": { "labels": ["foo", "bar"], },
        "error": null,
        "status": "Ok"
}
```

16. punctuation
```Python
def median(pool):
        copy = sorted(pool)
        size = len(copy)
        if size % 2 == 1:
            return copy[(size - 1) / 2]
        else:
            return (copy[size/2 - 1] + copy[size/2]) / 2
```

17. important
```CSS
body {
	    color: red !important;
}
```
```Markdown
# This is a heading. Headings are important.
```

18. comment
```Markup
<!-- Here's a comment -->
<style>
	/* Here's another comment */
</style>
<script>
// Here's yet another comment
</script>
```

19. tag
```Markup
<p>Hello World!</p>
```

20. attr-name, attr-value
```Markup
<p id="greeting">Hello World!</p>
<video width="1280" height="720" allowfullscreen controls>
        <source src="hello_world.mp4" type="video/mp4" />
</video>
```

21. namespace
```Java
class Foo extends foo.bar.Foo {
	    java.util.List<foo.bar.Foo.Bar> bar(foo.bar.Baz bat) {
            throw new java.lang.UnsupportedOperationException();
	    }
}
```

22. prolog
```Markup
<?xml version="1.0" encoding="utf-8"?>
<svg></svg>
```

23. doctype
```Markup
<!DOCTYPE html>
<html></html>
```

24. cdata
```Markup
<ns1:description><![CDATA[
  CDATA is <not> magical.
]]></ns1:description>
```

25. entity
```Markup
&amp; &#x2665; &#160; &#x152;
```

26. bold
```Markdown
    **I am bolded text!**
```

27. italic
```Markdown
    *I am italicised text!*
```

28. atrule
```CSS
@font-family {
        font-family: Questrial;
        src: url(questrial.otf);
}
@media screen and (min-width: 768px) { /* ... */ }
```

29. selector
```CSS
section h1,
#features li strong,
header h2,
footer p { /* ... */ }
```
