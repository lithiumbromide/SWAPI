---
title: "SetHeight Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "SetHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeight.html"
---

# SetHeight Method (INote)

Sets the height of this note in meters.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetHeight( _
   ByVal HeightIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim HeightIn As System.Double

instance.SetHeight(HeightIn)
```

### C#

```csharp
void SetHeight(
   System.double HeightIn
)
```

### C++/CLI

```cpp
void SetHeight(
   System.double HeightIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HeightIn`: Height for this note in meters

## VBA Syntax

See [Note::SetHeight](ms-its:sldworksapivb6.chm::/sldworks~Note~SetHeight.html).

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.html)
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.html)
[INote::GetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightInPoints.html)
[INote::SetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeightInPoints.html)
