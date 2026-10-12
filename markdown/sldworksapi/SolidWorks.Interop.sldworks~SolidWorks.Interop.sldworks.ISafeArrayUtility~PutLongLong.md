---
title: "PutLongLong Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutLongLong"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLongLong.html"
---

# PutLongLong Method (ISafeArrayUtility)

Adds the specified long long value to a Variant SafeArray of long long values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutLongLong( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Long _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Long

instance.PutLongLong(VariantArray, Index, Value)
```

### C#

```csharp
void PutLongLong(
   out System.object VariantArray,
   System.int Index,
   System.long Value
)
```

### C++/CLI

```cpp
void PutLongLong(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.int64 Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of long long values
- `Index`: Index of long long value
- `Value`: Long long value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetLongLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLongLong.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
