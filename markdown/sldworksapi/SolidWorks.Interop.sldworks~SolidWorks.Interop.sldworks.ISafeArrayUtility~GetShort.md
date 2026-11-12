---
title: "GetShort Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetShort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetShort.html"
---

# GetShort Method (ISafeArrayUtility)

Gets the specified short value in a Variant SafeArray of short values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetShort( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Short

value = instance.GetShort(VariantArray, Index)
```

### C#

```csharp
System.short GetShort(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.short GetShort(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of short values
- `Index`: Index of short value

### Return Value

Short value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutShort Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutShort.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
