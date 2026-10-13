---
title: "Get Last Save Error Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Last_Save_Error_Example_CSharp.htm"
---

# Get Last Save Error Example (C#)

```vb
This example shows how to get the last save error issued by Microsoft in the current SOLIDWORKS Design session.
  //-------------------------------------------------------------------
 // Preconditions:
 // 1. Open a SOLIDWORKS Design session and cause Microsoft to issue a save error.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Gets the last save error issued by Microsoft.
 // 2. Examine the Immediate window.
 //--------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
     {
        object varPath;
         object varError;
         object varMessage;
         long err;
        public void Main()
        {
            varMessage = swApp.GetLastSaveError(out varPath, out varError);
             if (!(varError == null))
             {
                 err = (long)varError;
                 if (!(err == 0))
                 {
                     Debug.Print("Document generating the save error: " + (String)varPath);
                     Debug.Print("Error code: " + (String)varError);
                     Debug.Print("Error message: " + (String)varMessage);
                 }
             else
             {
                 Debug.Print("This SOLIDWORKS Design session has not experienced a save error.");
             }
         }
        public SldWorks swApp;
    }
}
```
