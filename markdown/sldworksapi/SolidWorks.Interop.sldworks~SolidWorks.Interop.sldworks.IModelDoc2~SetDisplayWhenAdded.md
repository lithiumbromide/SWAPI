---
title: "SetDisplayWhenAdded Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetDisplayWhenAdded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html"
---

# SetDisplayWhenAdded Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::DisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~DisplayWhenAdded.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDisplayWhenAdded( _
   ByVal Setting As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Setting As System.Boolean

instance.SetDisplayWhenAdded(Setting)
```

### C#

```csharp
void SetDisplayWhenAdded(
   System.bool Setting
)
```

### C++/CLI

```cpp
void SetDisplayWhenAdded(
   System.bool Setting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Setting`: True to display new sketch entities when added, false to note

## VBA Syntax

See [ModelDoc2::SetDisplayWhenAdded](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetDisplayWhenAdded.html).

## Remarks

The sketch entities appear on the screen after performing [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) or [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) is performed. Also, [IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) must be True to use this method's settings.

This display setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to True at the end of your program. For example, if you have ended your program and the display is set to false, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

NOTES:

- IModelDoc2::GraphicsRedraw2 is much faster than ModelDoc2::EditRebuild3.
- IModelDoc2::SetAddToDB and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) also increase performance during sketch entity creation.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetDisplayWhenAdded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDisplayWhenAdded.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
