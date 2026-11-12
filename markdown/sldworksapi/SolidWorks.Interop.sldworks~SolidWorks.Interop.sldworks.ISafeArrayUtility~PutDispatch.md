---
title: "PutDispatch Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutDispatch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutDispatch.html"
---

# PutDispatch Method (ISafeArrayUtility)

Adds the specified Dispatch object to a Variant SafeArray of Dispatch objects.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutDispatch( _
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

instance.PutDispatch(VariantArray, Index, Value)
```

### C#

```csharp
void PutDispatch(
   out System.object VariantArray,
   System.int Index,
   System.object Value
)
```

### C++/CLI

```cpp
void PutDispatch(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.Object^ Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of Dispatch objects
- `Index`: Index of Dispatch object
- `Value`: Dispatch object

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetDispatch Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetDispatch.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
