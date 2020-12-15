# chatbot-no-ai

I am attempting to create a chatbot that learns but doesn't use things
like neural networks, just regular boring code. Also this is my first
time using GitHub, so please be nice!

## Requirements

> Note: if you are using the executable, there are no requirements.

-   Python 3 (and modules)
    -   nltk
    -   json
        > I don't know if this comes with python or if I just already
        > had it installed, please tell me if I don't need this

## Usage

After launching the program, type your "message" and press enter,
similarly to an instant messaging program. It will learn new responses
from your conversations, so keep that in mind. Once you are done, use
`Ctrl`+`C` to save and exit. `responses.json` is basically a save file,
so don't replace it if you are downloading a new version.

> Note: **don't** close the program using the `X` button, this will stop
> the program from saving anything it has learned in this session. On
> the other hand, use the `X` if you don't want to save anything it's
> learned.

## Editing the Save File

If you want to manually edit `responses.json`, you can do this using any
text editor (I reccomend notepad++, at it has useful syntax
highlighting.) It is in JSON format, with `message: response` pairs.
Since it is unlikely that a save file would contain every possible
message, the program looks for the saved message that most closely
matches the one it recieved, and sends the corresponding response. This
File is edited by the program whenever the program exits, so keep a
backup if you want.

## Todo

-   maybe include conversation history in response calculation (would
    probably make older save files worse)
-   add more utility modes (to help with homework)

## Notes

I realise that this already exists, but I just want to challenge myself.
Also, I'm putting it on GitHub because it's better than Google Drive for
this type of thing.
