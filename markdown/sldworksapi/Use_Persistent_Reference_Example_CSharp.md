---
title: "Use Persistent Reference Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Persistent_Reference_Example_CSharp.htm"
---

# Use Persistent Reference Example (C#)

Persistent references are a means of returning to an item between sessions of SOLIDWORKS Design. Persistent references are similar to attributes, but are easier to use. In almost all cases, persistent references can, and should, be used in place of attributes.

This example:

- shows how to use persistent references.
- is primarily diagnostic code that determines whether the currently selected item has a persistent reference from which an object can be retrieved.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part, assembly, or drawing.
 // 2. Select an entity.
 //
 // Postconditions:
 // 1. Gets the selected entity type and its PID.
 // 2. Examine the Immediate window.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace UsePersistentReference_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public string GetStringFromID(SldWorks swApp, ModelDoc2 swModel, byte[] vPIDarr)
         {
             string functionReturnValue = null;

             foreach ( int vPID in vPIDarr) {
                 functionReturnValue = functionReturnValue + vPID.ToString("###000");
             }
             return functionReturnValue;

         }

         public object GetObjectFromString(SldWorks swApp, ModelDoc2 swModel, string IDstring)
         {
             object functionReturnValue = null;
             ModelDocExtension swModExt = default(ModelDocExtension);
             byte[] ByteStream = new byte[IDstring.Length/3];
             object vPIDarr = null;
             int nRetval = 0;
             int i = 0;

             swModExt = swModel.Extension;
             for (i = 0; i <= IDstring.Length - 3; i += 3)
             {
                 int j;
                 j = i / 3;
                 ByteStream[j] = Convert.ToByte(IDstring.Substring(i, 3));
             }

             vPIDarr = ByteStream;

             functionReturnValue = swModExt.GetObjectByPersistReference3((vPIDarr), out nRetval);

             Debug.Assert((int)swPersistReferencedObjectStates_e.swPersistReferencedObject_Ok == nRetval);
             Debug.Assert((functionReturnValue != null));
             return functionReturnValue;

         }

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             ModelDocExtension swModExt = default(ModelDocExtension);
             SelectionMgr swSelMgr = default(SelectionMgr);
             object swSelObj = null;
             object swObj = null;
             byte[] vPIDarr = null;
             string sIDstring = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swSelObj = swSelMgr.GetSelectedObject6(1, -1);
             Debug.Assert((swSelObj != null));

             vPIDarr = (byte[])swModExt.GetPersistReference3(swSelObj);
             Debug.Assert((vPIDarr != null));

             Debug.Print("SelType = " + swSelMgr.GetSelectedObjectType3(1, -1));

             if ((vPIDarr == null))
             {
                 Debug.Print("  ModelDocExtension::GetPersistReference3 broken");
                 return;
             }
             else
             {
                 Debug.Print("  ModelDocExtension::GetPersistReference3 exists");
             }

             sIDstring = GetStringFromID(swApp, swModel, vPIDarr);

             Debug.Print("  Persist Ref = " + sIDstring);

             swObj = GetObjectFromString(swApp, swModel, sIDstring);

             if ((null != swObj))
             {
                 Debug.Assert(object.ReferenceEquals(swSelObj, swObj));
                 Debug.Print("  ModelDocExtension::GetObjectByPersistReference3 exists");
             }
             else
             {
                 Debug.Print("  ModelDocExtension::GetObjectByPersistReference3 broken");
             }

         }

         public SldWorks swApp;

     }
 }
```
