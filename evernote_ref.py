# Evernote test

import sys
sys.path.insert(0, '../Dev_Private')
from evernote_keys import *

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
import evernote.edam.userstore.UserStore as UserStore
import evernote.edam.notestore.NoteStore as NoteStore

dev_token = DEV_TOKEN
NoteStore_URL = NoteStore_URL

client = EvernoteClient(token=dev_token)

#CONSUMER API KEYS imported from external file, get these at evernote developer
client.consumer_key = CONS_KEY
client.consumer_secret = CONS_SECRET

userStore = client.get_user_store()
user = userStore.getUser()

noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
len(notebooks)

for note in notebooks:
  print note.name

nofilter = NoteStore.NoteFilter()
#nofilter.words = 'intitle"Word"'
spec = NoteStore.NotesMetadataResultSpec()

metadata = noteStore.findNotesMetadata(nofilter, 0, 1, spec)

guid = metadata.notes[0].guid

note = noteStore.getNote(guid, True, False, False, False)

print note.title
print note.content
print note.attributes


def new_note(title, content):
  emptynote = Types.Note()
  emptynote.title = title
  emptynote.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
  emptynote.content += '<en-note>'+content +'</en-note>'
  emptynote = noteStore.createNote(emptynote)
  return emptynote


# Eo File
