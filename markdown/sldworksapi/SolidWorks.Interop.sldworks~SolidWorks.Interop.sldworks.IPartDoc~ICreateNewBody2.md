---
title: "ICreateNewBody2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateNewBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.html"
---

# ICreateNewBody2 Method (IPartDoc)

Creates a new body to use for import sewing operations and returns it to the caller.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateNewBody2() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As Body2

value = instance.ICreateNewBody2()
```

### C#

```csharp
Body2 ICreateNewBody2()
```

### C++/CLI

```cpp
Body2^ ICreateNewBody2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartDoc::ICreateNewBody2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateNewBody2.html).

## Examples

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

## Remarks

The intention is that with a handle on such a (initially empty) body, appropriate construction methods (for example, [IBody2::CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html)) can be called that eventually amount to a non-trivial object.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::CreateNewBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateNewBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
