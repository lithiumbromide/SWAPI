---
title: "Apply and Remove Texture To and From Model By Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Model_Display_State_Example_CSharp.htm"
---

# Apply and Remove Texture To and From Model By Display State Example (C#)

This example shows how to apply and remove texture to and from a model by a display state.

```vb
 //------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified part and texture exist.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified part and applies texture to the part.
 // 2. Examine the part
 // 3. In the IDE, click the Continue button at
 //    System.Diagnostics.Debugger.Break().
 // 4. Removes the texture from the selected face.
 // 5. Examine the Immediate window and part.
 //
 // NOTE: Because the part is used elsewhere, do not save
 // changes.
 //----------------------------------------------------
```

```vb
using
```

SolidWorks.Interop.sldworks;

```vb
using
```

SolidWorks.Interop.swconst;

```vb
using
```

System;

```vb
using
```

System.Diagnostics;

```vb
    namespace
```

ApplyRemoveTextureByDisplayStateCSharp.csproj

```vb
    {
```

partial class SolidWorksMacro

```vb
         {
```

public void

Main()

```vb
             {
```

ModelDoc2 swModel = default(ModelDoc2);

```vb
ModelDocExtension swModelDocExt = default(ModelDocExtension);
Texture texture = default(Texture);
string displayState = null;
int errors = 0;
int warnings = 0;
string namStr = null;

 // Open document
```

```vb
swModel = (
```

ModelDoc2)swApp.**OpenDoc6**("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\motionstudies\\valve.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref

warnings);

```vb
swModelDocExt = (
```

ModelDocExtension) swModel.**Extension**;

```vb
// Set texture on model in the
```

// specified display state

```vb
displayState =
```

"<Default>_Display State 1"

;

```vb
namStr =
```

"<SystemTexture>\\images\\textures\\pattern\\checker2.jpg"

;

```vb
texture = (
```

Texture) swModelDocExt.**CreateTexture**(namStr, 5, 45, false

);

Debug.Print("Texture set: " + swModelDocExt.**SetTextureByDisplayState**(displayState, texture));

```vb
               // Examine the selected face to verify
               // that the specified texture was set
               // In the IDE, click the Continue button to resume
               // running macro
               System.Diagnostics.Debugger.Break();
```

```vb
// Remove texture from model by display state
```

Debug.Print("Texture removed: " + swModelDocExt.**RemoveTextureByDisplayState**(displayState));

```vb
// Rebuild model
```

```vb
swModel.ForceRebuild3(
```

false);

```vb
            }
```

```vb
/// <summary>
```

/// The SldWorks swApp variable is pre-assigned for you.

/// </summary>

public SldWorks swApp;

```vb
    }
```

}
