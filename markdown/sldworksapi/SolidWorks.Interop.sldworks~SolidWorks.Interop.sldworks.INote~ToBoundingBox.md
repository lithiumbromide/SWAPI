---
title: "ToBoundingBox Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "ToBoundingBox"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ToBoundingBox.html"
---

# ToBoundingBox Property (INote)

Gets and sets whether to select the **To bounding box** option for leaders in this note's PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToBoundingBox As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

instance.ToBoundingBox = value

value = instance.ToBoundingBox
```

### C#

```csharp
System.bool ToBoundingBox {get; set;}
```

### C++/CLI

```cpp
property System.bool ToBoundingBox {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to select the **To bounding box** option, false to not

## VBA Syntax

See [Note::ToBoundingBox](ms-its:sldworksapivb6.chm::/sldworks~Note~ToBoundingBox.html).

## Remarks

See the SOLIDWORKS Help for information about the **To bounding box** option.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
