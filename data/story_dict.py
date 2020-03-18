"""
Structure 
{
    "event_index" : { 
        "message" : "message to print (include line breaks!)",
        "options" :  {
            "message" : "message with options",
            "list" : list with integer values to check input
            }

    }
    ...
}
"""
STORY_DICT = {
    "a": {
        "message":
        "**********************************************************\n" +
        "As your eyes open you find yourself lying in bed in a big room." +
        " Book shelves, strange machinery, art and chemical apparatus is" +
        "found all over. You cant remember how you got there or why you " +
        "where there, but you sense strong comfort and familiarity with" +
        " the place in which youre in. Sat behind a table straight in " +
        "front of you is a Figure with grey hair apparently seems to be" +
        "writing something.\n",
        "options": {
            "message": "1-[Get out of bed]\n" +
            "2-[Wait and explore the room for further details]\n",
            "list": [1, 2]
        }
    }
}