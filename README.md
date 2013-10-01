romanize
========

Transcribe Greek text to Latin alphabet using the ISO 843:1997 standard (also known as ELOT 743:1987)

Usage
-----
It's a simple function, so you can just import it to your program and use it:

    from romanize import romanize
    print(romanize('Ελευθέριος Βενιζέλος'))
    
You can also use it as a standalone module:

    python romanize.py Ελευθερία ή Θάνατος
    
Or use it as a filter:

    python romanize.py < text_in_cp1253.txt
    


