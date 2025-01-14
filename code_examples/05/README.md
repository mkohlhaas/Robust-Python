### Advice

If you are just extending a type, such as adding new methods, you can subclass
directly from collections such as a list or dictionary.

If you need to write a more complicated class with the interface of another collec‐
tion type, use collections.abc. You will need to provide your own storage for
the data inside the class and implement all required methods, but once you do,
you can customize that collection to your heart’s content.

