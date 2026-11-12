---
title: "IGetParameter Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "IGetParameter"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.html"
---

# IGetParameter Method (IAttribute)

Gets the specified parameter on this attribute.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetParameter( _
   ByVal NameIn As System.String _
) As Parameter
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim NameIn As System.String
Dim value As Parameter

value = instance.IGetParameter(NameIn)
```

### C#

```csharp
Parameter IGetParameter(
   System.string NameIn
)
```

### C++/CLI

```cpp
Parameter^ IGetParameter(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Name of the parameter

### Return Value

[IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html)

## VBA Syntax

See [Attribute::IGetParameter](ms-its:sldworksapivb6.chm::/sldworks~Attribute~IGetParameter.html).

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.html)
