#TCA-Media Downloader 3 manual

TCA-Media Downloader 3 is a python-3-written program which is totally accessible with screen readers.

It is based on the YT-DLP library, which allows us to download multimedia content from hundreds of sites. [Here you can find out the officially supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md):



Besides, TCA-Media Downloader 3 uses FFMPEG, library which, combined with YT-DLP, allows us to convert our downloads to different formats.

TCA-Media Downloader 3 is mainly focused on YouTube, but as it's been said, it's compatible with many more sites, adding compatibility with some not official ones. The latter will depend on whether  YT-DLP can get the necessary info in order to download, that's to say, if it detects multimedia in the page we provide.

This manual, aims at describing the interface of TCA-Media Downloader 3 in its first version. New features added along the different updates will be reflected in the [Changelog] section (#changelog). New options and their description will be pointed out in such section, therefore, the main manual will only detail the first version.

Likewise, as we get an update, we'll try to provide a detailed description of the new changes included in such update.

TCA-Media Downloader 3 comes with an incorporated updater, which will provide us with program updates. Such updates will be divided into 3 sections, Library, Features and Complete.

1. Updates in the library branch: This branch will receive minor library updates and bug fixes.
2. Updates in the feature branch: This branch will receive updates of new features added to the program. Enhancements and improvements of previously implemented features will be in the library branch; this branch will only reflect new features.
3. Updates in the complete branch: This branch will receive complete program updates. This branch will update the entire components of the program and will be used to update it with new features, major bug fixes or critical libraries.

Upon checking for updates, in the description, the branch to wich the update belongs will be specified and we will always be able to know by the naming of the updated version.

TCA-Media Downloader in its first version will be 3.0.0.0, the first 0 belongs to the complete branch, the second one indicates the features branch, and the last one belongs to the library branch.

This manual will describe the main part of the program, letting the user explore it and discover all of the potential with which we've tried to provide TCA-Media Downloader 3 for our enjoyment by themselves.

In advance, we'll say that in this version, TCA-Media Downloader incorporates new download formats, more download options, new customization possibilities for the download and, something that a few programs have, not to say none.

We'll be able to search for videos, as in previous versions, but besides, we will now be able to search for playlists and channels quickly and simply, being able to interact with such results.

Likewise, in this version it's posible to have multiple downloads at the same time, being able to play symultaneously, while we keep using the program.

We expect to add new features already under development, and some in project.

In this first version we've tried to give you what  TCA-Media Downloader 2 had, but vitaminized and with new features in order to give you the most stable posible final version.

Once it's proved that the final version is stable enough, we'll begin adding new features that we think everyone will like.

##Interface description

In this first version we can say that the program is divided into 3 sections:

1. Tabs.
2. Player.
3. Controls.

###Tabs

In this first version we have 3 tabs, URL (Alt+1), Search (Alt+2) and downloads (Alt+3).

We'll be able to cycle among them with Alt+1, alt+2 and alt+3 keystrokes, as well as with Ctrl + Tab to go to the next tab or Ctrl + Shift + Tab to go to the previous tab.

We'll be able to know which tab we're in at any moment by pressing   the Ctrl+Space combination.
####URL (Alt+1)

This tab, when focused, will leave us in the fiel to enter a URL.

It will only work if it detects that what we've entered is an interned address, otherwise it won't do anything.

As i've mentioned, this program is mainly focused on YouTube, therefore, if we put a youtube URL, it will detect what kind of URL it is.

#####video, Playlist or Channel.

In case it's not a YouTube URL and it's from another compatible website, or if we wanna try to donload multimedia content from there, it will give us some other download possibilities.

Well, once we put a URL, if we press enter, A context menu with options related to such URL will be displayed. These options change depending on the kind of URL entered.

In a YouTuve video URL we'll have the following options:

* Regular download: This option will allow us to download the video with the options we have chosen (described later), it will add the download with a video property and with format (explained later), we'll be able to see the download in the downloads tab (Alt+3).
* Custom download: This option will open a dialog giving us the possibility to choose a format and see its properties. This is for advanced users who are familiar with audio and video codecs.
* Video info: this will open a dialog in which we will be able to view info and options for a video, such as copying diverse info to the clipboard, downloading and cheking info.
* Reproducir: Nos permitirá reproducir el vídeo en el reproductor incorporado en TCA-Media Downloader 3 (explicado más adelante).

In a YouTube playlist URL we'll have the following options:

* Download entire PlayList: This will add the whole playlist with all of its videos to download, with default options.
* Choose videos to download: This will open a dialog from which we'll be able to  check the videos we wanna download, dismissing those unchecked.

in this dialog we also have the following keystrokes in the list of videos:

* Space: checks or unchecks the selected item.
* Ctrl +P: the video will immediately play.
* Ctrl +D: the video will be immediately downloaded with the options we have set.
* Ctrl +I: will give us info about the position we are in the  playlist.
* Ctrl +F: this will open a dialog for us to write a position and move to it quickly in the list. This is helpful for those lists that have many videos.
*PlayList info: this will open a dialog in which we can view info about the playlist, whe'll have an area showing the videos such playlist contains as well as some options.
in this dialog, in the playlist videos section, we'll be able to press enter in each video and we'll get a context menu with the options that correspond to videos. Likewise, we have several keystrokes for each item in that list:

* Ctrl +P: this will play the video immediately.
* Ctrl +D: This will download the video immediately with the options we have set.
* Ctrl +I: will give us info about the position we are in the  playlist.
* Ctrl +F: this will open a dialog for us to write a position and move to it quickly in the list. This is helpful for those lists that have many videos.


In a youtube channel URL we'll have the following options:

* Download entire channel: this will add all the videos contained in the channel to download with the options we have chosen.
* choose videos to download: This will open a dialog allowing us to select the videos we want to download  by checking them, dismissing the ones we don't want. When this dialog opens, it may inform that the playlist has no videos. This may occur because the channel has the videos protected with copyright, videos are hidden, blocked by YouTube, password-protected or they are in different playlists rather than in the main part of the channel.

In this dialog we also have the possibility to use several keystrokes in the list of videos:

* Space: checks or unchecks the selected item.
* Ctrl +P: The video will play immediately.
* Ctrl +D: This will immediately download the video with the assigned options.
* Ctrl +I: This will give us info about our current position in the main channel playlist.
* Ctrl +F: This will open a dialog for us to write a position and move quickly to it within the playlist. this is helpful for those lists that have a lot of videos.
* Channel info: This will display a dialog with info about the channel and an area with 2 tabs, videos and Playlists, in which we can see what videos and what playlists the channel contains, respectively.

In any of these two areas, we can hit the enter key in an item and the corresponding options for videos or playlists will be displayed. In the videos area, we'll also be able to use  Ctrl+p to play, Ctrl+d to download, Ctrl+i to know where we are and Ctrl+f to move quickly to the item we want.

In this dialog we will also have different buttons in order to copy to the clipboard or download the channel.

If we enter a URL that doesn't belong to YouTube, upon pressing enter, the program will try to find multimedia content.

If it finds multimedia content  to download in the URL entered, It will give us two options: Try to download with format, which will try to download the file with the options we have set, and try to download original, which will try to Download the multimedia file in its original format.

If it doesn't find any multimedia content, it will tell us with a message.

The URL field can be quickly focused if we are in the URL tab with Alt + I.
Likewise, this URL field can also be cleared  with Ctrl +B if it has focus.

The following options in this tab will be those established for future downloads we perform, either by URl or by searching (explained later).

If we keep tabbing here, we'll land on a combo box called "select format": (Alt + F).

In this combo box we'll be able to choose different formats supported by the program, both video and audio. Besides, the last option in the box is advanced, which will allow new download options for what we choose to download.

If we tab again, we have the combo box asking us to choose the audio quality: (Alt + q) or choose a custom format advanced option: (Alt +C). This will occur if we have selected the advanced option in the format combo box.

In  audio cality we can select the desired vitrate for the downloaded audio. This will always depend on whether it's allowed by what we try to download, otherwise, if we put a high bitrate, it will always try to download the best audio quality.

If in the format combo box we have selected the advanced option, this box will offer 412 options, which don't always work in every audio or video that we wanna download. This is a matter of testing, and above all, this is for advanced users. It is reccommended that average users don't touch this option.

Each option has a description of what we try to download.

in this combo box we have 2 hotkeys:

* Ctrl + I: This will speak our current position in the combo box.
* Ctrl +F: This will open a dialog for us to quickly move to an option in the whole list.

If we keep tabbing, we'll land on a combo box called Choose output name composition: (Alt + N). Here we'll be able to choose the name of resulting files, also having the possibility to create a subfolder, Number the downloaded videos or audios, or not, by now.

Pressing tab once more, we'll land on a checkbox allowing us to choose the folder in which we wanna save downloads (Alt + U).

This box comes disabled by default, and will save our downloads in the  TCAMediaDownloader subfolder in the "music" folder by default, creating it if it doesn't exist.
We can check the box and a window will open, allowing us to choose the custom location for our downloads. If we uncheck the box when it is checked, The program will download in the default folder again.

That's all for the URL area.

####Search (Alt+2)

This tab has only two components:

Enter a search (Alt +S): Here we'll be able to put any kind of text and press enter in order to get options.

If we press enter while the field is empty, only one option will display: select number of results to show,  which is a submenu from where we can choose the number of results we wish to get, letting us choose between 10 and 500 results. This setting remains saved until we change it again.

If we enter some text and press enter, it will give us options to search for videos, playlists or channels, as well as the previous option to change the number of desired results. This will display as a context menu.

If we select any of the 3 first options, a search based on the term we have entered will be performed.

This search box can be quickly cleared with Ctrl +B, wich will clear both the search field and the results. We can also clear the search field with backspace and press enter. Then, a context menu will display with an option to clear search, which will clear the field and the list of results, and the previously mentioned option to change the number of results.

The menus are dynamic depending on the action we perform.

If we press tab, we'll land on a list called search results (Alt + R): In this list, we can press enter, and we'll get the same options already described in the URL tab for each search.

There are some options more if it's a video search.

We can use Ctrl + P to quickly play a video, Ctrl + D to download it, and besides, when we press enter on that video, we'll have the following new option in the menu:

Multiple search download: This option will open a dialog in which all of the search results will be displayed, letting us select the ones we wish to download.

This dialog is helpful in case we want to download several videos at once, rather than having to download one by one.

In this video list dialog  we can use space to check or uncheck, Ctrl +R to play and Ctrl + D to download the focused item. Besides, if we hit enter, we'll get menu options for videos, already explained above.

If we press tab, we'll land on an edit box in which we'll have to type the name for the multiple download. besides identifying the download, This name will create a subfolder with what we have put in our download folder, and everything we choose in this dialog will be downloaded to that subfolder.

That's all for the search tab.

####Downloads (Alt+3)

This tab is also simple, with two controls.

There's a list containing our downloads, which we can access with Alt+ L, and if we press tab, there's a read-only field called status (Alt + E). There's also a progress bar that will speak the status of the download we've chosen in the list.

In the download list, the type of download will be spoken. video, playlist, channel or other, as well as its format. The format will depend on what we have selected in the URL tab. También el nombre de la descarga.

If we press enter on a download, a menu with options will be displayed. This menu is dynamic depending on the downloads and their status.

If the download is in progress, this menu will allow the following:

* Play (only video downloads)
* Open download link on the web
* Copy download link to clipboard

If the download is completed, the offered options would be:

* Open download folder
* Besides, if there are completed downloads, a menu called general actions will allow:
* Clear completed downloads

* If an error occurs and we have the related download selected, it will give us the option to view the error, consisting of a dialog with the related error and the possivility to copy such error message to the clipboard.

In the general actions submenu, we will also get an option to clear failed downloads, if any.

If we press tab, we'll land on the read-only field that displays some info about the status of the download and what is being done.

The downloads tab finishes here.

###Player

In this section, if we press tab and nothing is playing, the program will jump to the following section (Controls), since this option only contains the playback buttons when it is active.

The buttons are:

* Rewind (F1)
* Play (F2) or Pause (F2) Depending on its status.
* Fast-forward (F3)
* Stop (F4)

Both in the rewind button (F1) and in the fast-forward button (F3) we can press the aplications key, Shift F10 or Ctrl + M, to get a menu, which will allow us to select the rewind or fast-forward time for the track we are playing.

The option we choose in that menu will be selected until it's changed again.

The player can be controlled with the shortcuts indicated above, from anywhere in the program except the settings or updates dialog.

In these two dialogs, where the player cannot be controlled, when they're opened, playback will be paused until they're closed.

Take into account that if any of the actions in these dialogs need to restart the program, playback will stop, and we'll have to resume it if we wish.

###Controls

In this section, we will find:

####Volume: (F5 / F6):
With this keys, we will turn the volume up or down. If we press Alt + V and the control has focus, with left, right, down or up arrows, we will turn the volume down or up respectively.
####Speed: (F7 / F8):
we can also press Alt + V to focus this control.  This combination will toggle between volume and speed, depending on what control has focus. 
* With f6 or f7 or the arrow keys, we'll decrease or increase playback speed. We gotta be careful, because if we put to much speed, the playback buffer may run out of data and give an error message. This doesn't happen with all videos, and it also depends a lot on the internet conection we have.
####Audio output:
We can quickly focus this combo box with Alt + S, but such control will only be available if playback is active, either playing or paused. 
We'll be able to choose through which device we want the sound to play.
It should be clarified that when playback stops, the device goes back to defaults, therefore, if we want another device for next playback, we'll have to select it again. Currently, this option can't be saved due to technical reasons.
If a solution is found in the future, the user will be allowed to choose through which device they want the sound to play.
####Video screen (F11):
If playback is active, either playing or paused, we can also have quick access to the control with Alt + P. The control is a checkbox  that, when checked with space, wil show us a full screen with the video, being able to watch its content. By default, the video comes disabled, playing audio only, but at any moment and from any dialog, we can enable the video screen with F11, eccept in the settings and updates dialogs. the video screen also supports F1 to rewind, F2 to play / pause, F3 to fast-forward, F4 to stop and close the screen, F5 and F6 to turn volume up or down, F7 and F8  to increase playback speed and keys explained later. It should be said that this screen can be closed continuing playback with escape, or it closes automatically if it loses focus. The latter means that if we are in the video screen and we press Alt + Tab, the window will close upon losing focus.

###Menu buton (Alt + M):
this menu will contain different tools, options and general actions. in this first version, it contains the followin:

####Check for updates:
This will search for updates; if there are no updates, it will inform us, otherwise, a dialog will display giving us the possibility to update. It should be said that, this option can only be invoked if we have no active downloads.
####Options:
This will open a dialog with program settings (explained in the following section)
####Manual:
Opens this documentation in our default browser.
####Visit our website:
Opens the blog's main page.
####About...:
Displays info about the version of the program, version of libraries and the version of python with which the program was compiled.
####Exit:
Exits the program, checking first if we have any active downloads. In this case, we'll be warned with a dialog where we'll need to choose if we really wanna exit. We can also exit with Alt + F4 from the main interface.

###Options dialog

This dialog has different areas in this first version.

When we open it, the focus will be on a list where the different areas are, so we can move with up or down arrows.

New sections and options will be added to this dialog as the program includs new features.

When we are in the desired area,if we press tab, we'll land on the options for that area, and we can move through them with tab.

In this first version, the following options are offered:

####General:
This area contains general options, whose options are:

#####Change program language:
Pressing this button  will give us a menu with the languages the program supports. Currently, 85 languages are supported, from which in this first official version, only spanish and english are official and the rest of languages are generated by an automatic translator. In a following section of this document, we'll explain how it works, and how the one who likes can add a language and make it official for the program. later, I'll talk about languages and give technical info for translators.
#####Choose the program's home tab:
In this combo box we can Select the tab that will be loaded when the program stars.
#####Minimize to system tray When the main window is minimized:
If we enable this box and minimize the window, instead of staying minimized, it will hide into system tray, and a new icon with the name TCA-Media Downloader and its version appears. If we press the icon directly, the  TCA-Media Downloader window will open; If we press the left button, it will give us a menu to open or close the program, and if we double click, the program will open. this will have new options in the future. the icon will only appear when the program is hidden. In case it's restored, the icon will disappear from the system tray.
####Downloads:
Here we'll add those options referred to downloads.

Currently, we have:

#####Resume incomplete downloads (experimental):
If we check this box, A dialog will display explaining how this works, but all in all, what wil happen is that, if we close the program and there were active downloads left, If we put the same URL or search and download again, and traces of such download are detected, rather than starting over, it will try to download from where it was interrupted.

It should be said that this option is in experimental mode and that there's no warranty that it works in all cases.

####Player:
Here we'll put what concerns the player.

It currently brings the following:

#####play the best quality (Quality menu won't be displayed when pressing play):
By default, this box is checked, therefore, when we play a video, the best quality found will always be played. If we uncheck this box, pressing play on a video will give us a menu from which we can select the playback quality, low, medium or high, as long it's available. in some videos for example, it can give us only low and medium, low and hig, or medium and high quality. it all depends on what calities are found.

This is to the user's liking. this setting was added for those users with limited connections so that they can have the possibility to choose if they uncheck the box, for example, choosing low quality in order to save connection data.
#####Show video screen when playing:
This box is unchecked by default.

If we check it, When a video starts playing, the video screen will open automatically.

In this screen we'll be able to use playback keys from F1 to F12.

It should be said that the video screen  will close if it loses focus, and we'll have to open it again in order to continue watching the content visually.
####Sound:
Here we'll be able to customize which sounds we want to play and whixh ones not.

Currently, we can enable or disable the following:

* Play startup sound (This will play when the program loads slowly)
* Play waiting sounds (Will play in waiting dialogs)
* Play new download sound (will play upon adding a new download)
* Play successful download sound
* Play failed download sound
* Send action information mesages to screen reader

We can select the mentioned boxes for them to sound or not. They all come checked by default.


Something should be said about sending action information messages to screen reader: This option will give us info about the different actions performed in the program, for instance, when we press Ctrl + B in the URL field, it will say URL field cleared. This will be spoken by the screen reader itself.

Also in the player keys, turning volume up or down, or or in the speed controls for instance, it will say turning volume 95% up, or playing, pausing, fast-forwarding 30 seconds, etc. 
These are messages sent to the screen reader if the box is enabled, if not, these messages won't come out.

There are three key combinations that, although we have the box unchecked, will be sent to the reader. These are:

* F9: will tell us the elapsed and total times of the playing track. If there's none, It will thell us that nothing is playing.
* F10: will tell us the title of the playing track, if there's nothing, it will inform us accordingly.
* Ctrl + O: This combination will give us quick info about the download options we have set in the URL tab.
* Ctrl + S: This combination will provide us with information about active, completed, and failed downloads.

this keystrokes can be called and used anywhere in the program, except in settings and updates.

also, after the boxes for sounds, we have the following combo box:

#####sound preview (select a sound and press ctrl+r to play it):
In this box, if we press Ctrl + R, it will give us the sound's preview, so that we can identify the sounds of the program.

And finally, this options dialog has the OK and cancel buttons.

If we press OK, changes will be saved, and if we press cancel, nothing will be changed.

It should be warned that language changes require that the program is restarted and that this change will only happen if there are no active downloads.

##Summary of important keys

###For the player:

* F1: Rewind
* F2: Play / Pause
* F3: Fast-forward
* F4: Stop
* F5: Volume down
* F6: Volume up
* F7: Speed down
* F8: Speed up
* F9: Elapsed / total time
* F10: Title of playback in progress
* F11: Enable or disable video screen
* F12: Enable or disable messages spoken by the screen reader
* Ctrl + M: Shows the menu for choosing rewind and forward time, only in such player buttons

###In video lists:

* Ctrl + R: Play
* Ctrl + D: Download
* Ctrl + I: Position in the list
* Ctrl + F: Dialog for moving to a position in the list
* Enter: action on the focused item and other options depending on where we are
* Space: only in selection lists, will check or uncheck the focused item

###Rest of non-video lists and text fields:

* Ctrl + B: Clears text fields
* Enter: Displays the menu with the corresponding options depending on where we are

###Custom format combo box::

* Ctrl + I: reports the position in the combo box
* Ctrl + F: Displays the dialog to choose where we wanna turn to in the combo box

###Waiting dialog:

In the waiting dialog that appears each time you perform an action, there is a special panic keystroke.

Such combination is:

Shift + Ctrl + Alt + K

This combination is experimental and should only be used in case the waiting dialog takes too long and the program doesn't perform the requested action.

Use only in  specific cases and when this dialog remains for too long.

###Others:

* Ctrl + O: will give us format, quality, name and location info.

These are the options we have set in the URL tab and are those set for downloads.

* Ctrl + S: Donload status info

Will tell us with a message in our reader if there are any downloads or not.

If so, it will tell us the number of active, completed and failed downloads.

This keystroke works anywhere in the program except in the updates, settings, waiting or position dialog.

##Info about program languages

As mentioned previously, in this first version, only spanish and english languages are official, while the other 83 are automatically generated by a machine translator.

If someone wants to contribute with an official language,  the following steps must be followed.

All languages are in the DATA/LOCALE folder. you only have to go to yours and change the base.po file.

You can delete the automatic translation and make your own, or correct the automatic one. Then save the changes and generate the .po file. This way the language will reflect your changes once you restart.

If you wanna make it oficial, send us the base.po via the contact channels in the  Tecnoconocimiento Accesible blog.

If your language is not among those included, you can still add it.

in the  DATA/LOCALE folder there is a file called main.pot; you can open the file and generate a .po template for your language.

Then, you only need to follow the same folder structure  for adding your language and sabe the base.po with your translation in the folder for the new language that will be added.

Next time you open the program you can then choose your language.

You can still send the base.po with the new language to the blog's contacts and the new language will be officially added.

It should be warned that in those updates whose description says that languages will be updated, if we have made any changes on our own, such changes will be overwritten by those of the update. therefore, we recommend that you save any change you have made  and then coppy it again mannually.

otherwise, the update will delete any change that is not official.

If changes are official, they won't be lost.

It should be also said that only official translations will be supported, with no warranty that automatic translations work correctly or that they are perfect. on the contrary, they're likely to have a lot of mistakes, but in most cases, it can help so that the user who doesn't handle another language can partially use the program in their language .

## technical observations

in the  DATA/LOGS folder, the program will sabe debug files.

These files contain info about errors that can occur, so we strongly recommend that these files are attached upon reporting a bug.

When an error occurs, try to see exactly at what time it happened, since it is saved in the log files. so if the file has more than one error, with those files and the time the error occurred, it is easier to detect.

We have tried so that the program has protections for it not to get frocen or unusable, and we've tried to contemplate the majority of errors that can occur.

but it should be understood that it's not possible to contemplate them all, so with the different updates that are performed, we'll try to make the program more robust each time.

it should be also be warned about the abuse of adding downloads. each Downloadwe add requires resources, so if we put too many downloads,  and our computer doesn't have enough resources, we can block the computer.

Use with responsibility and taking into account that each download requires ram and bandwidth.

##Observations
Occasionally, we can run into channels that don't seem to contain videos.
In this case, we'll do the following:

1. to go back to search results, press escape
2. On the channel result, press enter and access its info.
3. Once there, move to the "channel lists" tab with ctrl + Tab
4. Here we'll be able to find the channels, if any, and choose the videos to download from such channel.

#Credits

I wanna give special thanks to beta testers, Gera, Gustavo, Peter, Pepe, Rosa, Romina, Rayo, Óscar, Simone and anyone I'm likely forgetting. My appologies.

Likewise, to official translators:

* Italian: Simone Dal Maso
* Turkish: Umut Korkmaz
* English: Slann Tonic

#Changelog.<a name="changelog"></a>

It should be remembered that in this section, new features will be added without modifying the main document  as an orientation as updates come out.

Therefore, once we are familiar with the program in its first version, it's recommendable to visit this section in order to see what's new, since here we'll point out new features, their description and keyboard shortcuts.

Only update versions belonging to feature and complete branches will be added.

The library branch will comprise bug fixes and internal libraries, without changing anything about handling the program.

The user is responsible of checking this section in order to be informed about changes.

## Version 3.0.1.0.

* New tab called Favorites (Alt + 4).
Now we can save videos, playlists, or channels that we want in this tab for quick access.
When we open this tab, we will have 3 sections:
Alt + F: Takes us to the tree where we can interact with the branches.
The tree has a base called Favorites, and if we press Enter, we can delete the entire database or create and restore a backup of the database.
There is a branch called Videos, and if we press Enter, we can create video playlists. Pressing this option will open a window to enter the name of the playlist.
Once we have added video playlists, we can expand the branch, and we will have sub-branches. If we press Enter on a sub-branch, we will have the option to edit, delete, or clear that video playlist.
We also have two branches in the tree called Playlists and Channels. If any of these branches have content, we can press Enter on them to delete their content.
Alt + C: Takes us to the content area. In this area, the content of the selected video playlist, playlist, or channel will be displayed.
In this area, if we press Enter on an item, a corresponding menu for videos, playlists, or channels will appear, allowing us to interact with them.
Alt + B: Takes us to a search box where we can search within the selected branch. In this box, we can enter the search query in lowercase or uppercase and press Enter to get the result in the query area. We can interact with the result by pressing Enter on it.
The search field allows us to enter partial text. For example, if we search for "TCA," it will return all videos in the current branch that contain those letters.
We can reset the search to its original values and quickly restore the content area by pressing Ctrl + B in the search box or by deleting the entered text and pressing Enter. Additionally, if there is an ongoing search in the content area, pressing Ctrl + B will reset it to its original values.
To add content to the database, we do it from the information of each branch. For example, if we want to add a video to a playlist we have created from the search tab, when we have search results, we press Enter on the item and click on "Video Information." In the opened window, there will be a button called "Add to Video Playlist," which, when clicked, will display a menu with all the video playlists we have created in the database. If we choose one, the video will be saved in that playlist.
We can add the same video to multiple playlists, but it can only be added once per playlist.
Regarding playlists and channels, the process is similar. In the information dialog, there is a button called "Add to Favorites." Clicking on it will add the playlist or channel to the corresponding branch in the database. The button will then change to "Remove from Favorites." Unless we delete the playlist or channel from the Favorites tab or from the information dialog, it will remain in the database.
The playlist and channel branches will only store one item each, but multiple items with the same name can be stored as long as the URLs are different.
In the query area, we can press Ctrl + I to know our current position and Ctrl + F to quickly navigate to the desired item.
The possibility of adding to the database from search results has been added.
Now we can press Enter on a video, playlist, or channel in the search results, and the last option in the context menu will allow us to interact with the favorites database.
We will have the same options as in the video, playlist, or channel information dialogs.

* Added Ctrl + R and Ctrl + D in the URL field.
Now, in the URL tab, if we enter a YouTube video URL, we can press these combinations to play or download the video without the need to open the context menu.

* Added the ability to view comments on a video (experimental).
Now, when we open the video information dialog, a button will appear if the video has comments.
The button is called "View or Save Comments," and if we click on it, we can view or save the comments.
These options are experimental, and it has been detected that they may occasionally close the application. If there are ongoing downloads, the user will be notified that they may lose the information being downloaded.
If we choose to view comments, a comments extraction window will appear, indicating the percentage of comments extracted. We can cancel the extraction by clicking the cancel button in the window.
Once the extraction is complete, a window will open with all the comments, displayed in a tree control.
We can expand the tree and navigate through the comments. If a comment has replies, we can also expand it to view the replies.
Long comments will be marked with ** at the end, indicating that the full comment does not fit.
To have the comment read aloud by a screen reader, there is a key combination: Ctrl + T.
Similarly, if we press the Tab key, we will enter a read-only box where we will have the complete comment along with the name of the commenter, the date, and the number of likes.
In this window, there is a button called "Save," which performs the same action as in the video information dialog's context menu: it saves the comments in an accessible HTML format.
The structure of the HTML is as follows:
Heading Level 1 for the video title.
Heading Level 2 for the main comment.
Heading Level 3 for comment replies.
The entire window has shortcuts to navigate quickly:
Alt + L: Takes us to the comment tree.
Alt + D: Takes us quickly to the details of the focused comment.
Alt + G: Saves the comments as an HTML file.
Alt + C, Alt + F4, or Escape: Closes the window.

* New functions in context menus and improvements.
Context menus in the download area have been corrected. The "Play" option no longer appears for items that are not videos.
The issue where the multiple download menu did not appear when there was only one video result or one video in the database has been fixed.
New options have been added to the context menus based on the context, such as:
Open in Web: This option opens the selected video, playlist, or channel in our browser, taking us to YouTube.
A sub-menu called Share has been added.
This menu allows us to share the URL with Twitter, Facebook, Telegram, WhatsApp, Mastodon, or as a QR code with our mobile device.
If we choose "Generate QR Code to Open with Mobile," a window will open in the center of the screen displaying a QR code. Once our mobile device's QR code reader detects it, the URL, whether it's for a video, playlist, or channel, will open on our device.
Note that on Facebook, it only allows sharing the URL, so we cannot automatically add text. However, on the screen it redirects us to, we can manually add information.
For Mastodon, it will ask for the URL of the instance we are on. We can save or modify it if desired. If we save it, it will be pre-defined, and we won't have to add it each time we want to share with Mastodon.
Note that to share on any social network, we need to be logged into our browser session. Sharing will be easier if we have the WhatsApp and Unigram applications installed.

* Added new options in the settings dialog.
In the General category, the following has been added:
Check for Updates and Notify: In this dropdown box, we can choose whether we want the application to check for updates and notify us with a Windows notification.
We can choose to disable this option or select different time intervals for the application to check for updates.
When an update is found, a Windows notification will inform us about the update and its version.
This option does not download updates; it only checks for updates at the selected intervals. To download updates, we have to manually check for updates.
Notifications will continue to appear at the selected time intervals until we update the application.
In the Downloads category, the following has been added:
Time to Extract Information (if the extraction time exceeds, it will display an error if all the information was not obtained, valid for large playlists or channels): In this dropdown box, we can increase the time it takes for the application to determine that it couldn't retrieve all the information.
By default, it is set to 2 minutes, which is a reasonable and sufficient time for most playlists and channels.
If more time is needed, for example, for playlists or channels with more than 5000 videos, we can increase the data retrieval time.

* Added protection against downloading live streams in all dialogs.
A protection has been added to detect if the URL we want to download is for a live stream. In such cases, it will not allow us to download the live stream.
This issue has been addressed, and an alternative solution will be provided in future versions.

* Updated internal libraries for better application performance.

* Fixed internal errors.

* Updated translations.

## Version 3.0.0.0.

* Initial version.
