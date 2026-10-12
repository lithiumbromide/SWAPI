---
title: "CreateNewBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "CreateNewBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateNewBody.html"
---

# CreateNewBody Method (IPartDoc)

Creates a new body to use for import sewing operations and returns it to the caller.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateNewBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Object

value = instance.CreateNewBody()
```

### C#

```csharp
System.object CreateNewBody()
```

### C++/CLI

```cpp
System.Object^ CreateNewBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

New [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [PartDoc::CreateNewBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~CreateNewBody.html).

## Examples

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)
[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)
[Create Imported Solid Body (C#)](Create_Imported_Solid_Body_Example_CSharp.htm)
[Create Imported Solid Body (VB.NET)](Create_Imported_Solid_Body_Example_VBNET.htm)
[Create Imported Solid Body (VBA)](Create_Imported_Solid_Body_Example_VB.htm)

## Remarks

The intention is that with a handle on such a (initially empty) body, appropriate construction methods (for example, [IBody2::CreateTrimmedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateTrimmedSurface.html)) can be called that eventually amount to a non-trivial object.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ICreateNewBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.html)
