---
title: "InsertAxis2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertAxis2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertAxis2.html"
---

# InsertAxis2 Method (IModelDoc2)

Inserts a reference axis based on the currently selected items with an option to automatically size the axis.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAxis2( _
   ByVal AutoSize As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AutoSize As System.Boolean
Dim value As System.Boolean

value = instance.InsertAxis2(AutoSize)
```

### C#

```csharp
System.bool InsertAxis2(
   System.bool AutoSize
)
```

### C++/CLI

```cpp
System.bool InsertAxis2(
   System.bool AutoSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AutoSize`: True if axis is to be automatically sized, false if not

### Return Value

True if the reference axis is created successfully, false if not

## VBA Syntax

See [ModelDoc2::InsertAxis2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertAxis2.html).

## Examples

[Create Revolve Features (VBA)](Create_Revolve_Features_Example_VB.htm)
[Create Revolve Features (VB.NET)](Create_Revolve_Features_Example_VBNET.htm)
[Create Revolve Features (C#)](Create_Revolve_Features_Example_CSharp.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
