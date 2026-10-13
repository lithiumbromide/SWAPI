---
title: "GetAttributeValue Method (IBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "IBlockInstance"
member: "GetAttributeValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~GetAttributeValue.html"
---

# GetAttributeValue Method (IBlockInstance)

Obsolete. Superseded by [ISketchBlockInstance::GetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAttributeValue( _
   ByVal TagName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockInstance
Dim TagName As System.String
Dim value As System.String

value = instance.GetAttributeValue(TagName)
```

### C#

```csharp
System.string GetAttributeValue(
   System.string TagName
)
```

### C++/CLI

```cpp
System.String^ GetAttributeValue(
   System.String^ TagName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TagName`:

## VBA Syntax

See [BlockInstance::GetAttributeValue](ms-its:sldworksapivb6.chm::/sldworks~BlockInstance~GetAttributeValue.html).

## See Also

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.html)
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.html)
