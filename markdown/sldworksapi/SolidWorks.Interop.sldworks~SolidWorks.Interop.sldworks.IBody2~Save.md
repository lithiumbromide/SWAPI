---
title: "Save Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Save"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Save.html"
---

# Save Method (IBody2)

Saves this body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Save( _
   ByVal StreamIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim StreamIn As System.Object

instance.Save(StreamIn)
```

### C#

```csharp
void Save(
   System.object StreamIn
)
```

### C++/CLI

```cpp
void Save(
   System.Object^ StreamIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StreamIn`: Stream to use for the save

## VBA Syntax

See [Body2::Save](ms-its:sldworksapivb6.chm::/sldworks~Body2~Save.html).

## Remarks

If you want to save the solid body associated with the document, then save the document.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ISave Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ISave.html)
[IModeler::IRestore2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IRestore2.html)
[IModeler::Restore Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~Restore.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
