# ToddHash
The Todd Wellman Signature Hashing Method

=================Back Ground Story======

This program is inspired by my roomate and friend, Todd Wellman.

Almost all computer science courses at RIT require the student to use version control. To prove that a student used the version control, typically git, they have them create a log file called 'revisions.txt'

Todd Wellman, however, likes to live dangerously. Todd Wellman doesn't use version control, so he can't create a git log. So, he is forced to fake his git logs. And to do this, Todd employs his signature 'toddHash' to fake the hash values.

Todd uses a primitive method of smashing his fingers on the keys until it looks like forty random characters. My patented Todd Hash, however, will create a git log with a completed randomized hash value to fool any professor!

The program is a python script that takes in a file that you are supposed to have version control for and pulls method names from it. The function then generates a fake git log with a 'final' and 'initial' commit, and a 'modified "methodname"' commit in between.


=================Functionality=====

ToddHash.py currently only handles faking python commits. Java and C implementation will be developed soon.
To run program navigate to the folder with desired file to fake commits for and run:

  python3 ToddHash.py file.py firstName lastName email startDate(dd/mm/yy) endDate(dd/mm/yy) numberOfCommitsToFake
  
and it will print out to the terminal a faked git log.
To fake a revisions.txt simply append '> revisions.txt' to pipe the output to a txt file.

A fake python file is provided to test the ToddHash
