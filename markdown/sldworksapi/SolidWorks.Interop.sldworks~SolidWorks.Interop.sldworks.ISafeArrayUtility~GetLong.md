---
title: "GetLong Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetLong"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLong.html"
---

# GetLong Method (ISafeArrayUtility)

Gets the specified long value in a Variant SafeArray of long values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLong( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetLong(VariantArray, Index)
```

### C#

```csharp
System.int GetLong(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetLong(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of long values
- `Index`: Index of a long value

### Return Value

Long value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLong.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
