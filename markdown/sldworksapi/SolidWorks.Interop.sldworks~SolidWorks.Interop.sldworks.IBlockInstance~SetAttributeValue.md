---
title: "SetAttributeValue Method (IBlockInstance)"
project: "SOLIDWORKS API Help"
interface: "IBlockInstance"
member: "SetAttributeValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~SetAttributeValue.html"
---

# SetAttributeValue Method (IBlockInstance)

Obsolete. Superseded by [ISKetchBlockInstance::SetAttributeValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAttributeValue( _
   ByVal TagName As System.String, _
   ByVal Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBlockInstance
Dim TagName As System.String
Dim Value As System.String
Dim value As System.Boolean

value = instance.SetAttributeValue(TagName, Value)
```

### C#

```csharp
System.bool SetAttributeValue(
   System.string TagName,
   System.string Value
)
```

### C++/CLI

```cpp
System.bool SetAttributeValue(
   System.String^ TagName,
   System.String^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TagName`:
- `Value`:

## VBA Syntax

See [BlockInstance::SetAttributeValue](ms-its:sldworksapivb6.chm::/sldworks~BlockInstance~SetAttributeValue.html).

## See Also

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.html)
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.html)
