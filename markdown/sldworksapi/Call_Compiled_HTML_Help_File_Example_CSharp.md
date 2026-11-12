---
title: "Call Compiled HTML Help File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Call_Compiled_HTML_Help_File_Example_CSharp.htm"
---

# Call Compiled HTML Help File Example (C#)

This example shows how to call a compiled HTML Help file.

```vb
'-------------------------------------
'
' Preconditions: Specified compiled HTML Help file exists.
'
' Postconditions: Compiled HTML Help file is displayed.
'
'-------------------------------------
public bool OnHelp()
            {
                  string url = "E:/am/2005/C#/DisplayHelpFromPropMgr/apihelp.chm";

                  //Create a basic form to be the basis for the Help file
                  System.Windows.Forms.Form helpForm = new System.Windows.Forms.Form();
                  System.Windows.Forms.Help.ShowHelp(helpForm, url);
                  return true;
            }
```
