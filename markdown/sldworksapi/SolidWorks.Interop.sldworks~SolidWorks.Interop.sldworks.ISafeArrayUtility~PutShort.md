---
title: "PutShort Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutShort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutShort.html"
---

# PutShort Method (ISafeArrayUtility)

Adds the specified short value to a Variant SafeArray of short values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutShort( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Short

instance.PutShort(VariantArray, Index, Value)
```

### C#

```csharp
void PutShort(
   out System.object VariantArray,
   System.int Index,
   System.short Value
)
```

### C++/CLI

```cpp
void PutShort(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.short Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of short values
- `Index`: Index of short value
- `Value`: Short value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetShort Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetShort.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
