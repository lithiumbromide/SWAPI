---
title: "GetParameter Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.html"
---

# GetParameter Method (IAttribute)

Gets the specified parameter on this attribute.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParameter( _
   ByVal NameIn As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim NameIn As System.String
Dim value As System.Object

value = instance.GetParameter(NameIn)
```

### C#

```csharp
System.object GetParameter(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.Object^ GetParameter(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Name of the parameter

### Return Value

Object for the parameter

## VBA Syntax

See [Attribute::GetParameter](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetParameter.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feautre and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.html)
