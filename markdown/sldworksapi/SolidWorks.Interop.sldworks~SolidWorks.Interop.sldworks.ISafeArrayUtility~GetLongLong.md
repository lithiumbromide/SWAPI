---
title: "GetLongLong Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetLongLong"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLongLong.html"
---

# GetLongLong Method (ISafeArrayUtility)

Gets the specified long long value in a Variant SafeArray of long long values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLongLong( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Long

value = instance.GetLongLong(VariantArray, Index)
```

### C#

```csharp
System.long GetLongLong(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.int64 GetLongLong(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of long long values
- `Index`: Index of long long value

### Return Value

Long long value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutLongLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLongLong.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
