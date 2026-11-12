---
title: "PutLong Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutLong"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutLong.html"
---

# PutLong Method (ISafeArrayUtility)

Adds the specified long value to a Variant SafeArray of long values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutLong( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Integer

instance.PutLong(VariantArray, Index, Value)
```

### C#

```csharp
void PutLong(
   out System.object VariantArray,
   System.int Index,
   System.int Value
)
```

### C++/CLI

```cpp
void PutLong(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.int Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of long values
- `Index`: Index of long value
- `Value`: Long value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetLong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetLong.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
