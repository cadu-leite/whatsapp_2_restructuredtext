whatsapp_exp2pdf
================


Whatsapp files export to PDF


Use 
===

- Export conversation from whatsapp
- Copy the files to a directory on your computer
- You may not have other ".txt" on same directory, the one found there will understood as the conversation file.
- Pictures will be linked using RestructuredText `img` directive
- Audio files will be just linked for now. 


positional arguments:
  input                 whatsapp text file name (a `.txt` file) - remember to use quotes (") for filename with spaces

optional arguments:
  -h, --help            show this help message and exit
  -m MEDIAPATH, --mediapath MEDIAPATH
                        path for media files
  -o OUTPUT, --output OUTPUT
                        output file name - generated ResructuredText



sample
------

simple call

.. code-block:: bash

    $> python3 -m zap2rst 'my conversation file with soebody.txt'

If media files are at other path use `-m` asrgs to inform the path

.. code-block:: bash

    $> python3 -m zap2rst -m /mediapath/medias 'my conversation file with soebody.txt'

    >>> Output generated: output.rst

you may specify an output file name 

.. code-block:: bash

    $> python3 -m zap2rst -o myconversation.rst 'my conversation file with soebody.txt'

    >>> Output generated: output.rst
