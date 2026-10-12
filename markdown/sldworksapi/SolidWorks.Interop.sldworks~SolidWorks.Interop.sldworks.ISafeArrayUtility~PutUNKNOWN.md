---
title: "PutUNKNOWN Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutUNKNOWN"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutUNKNOWN.html"
---

# PutUNKNOWN Method (ISafeArrayUtility)

Adds the specified UNKNOWN object to a Variant SafeArray of UNKNOWN objects.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutUNKNOWN( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Object

instance.PutUNKNOWN(VariantArray, Index, Value)
```

### C#

```csharp
void PutUNKNOWN(
   out System.object VariantArray,
   System.int Index,
   System.object Value
)
```

### C++/CLI

```cpp
void PutUNKNOWN(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.Object^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of UNKNOWN objects
- `Index`: Index of UNKNOWN object
- `Value`: UNKNOWN object

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetUNKNOWN Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetUNKNOWN.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
