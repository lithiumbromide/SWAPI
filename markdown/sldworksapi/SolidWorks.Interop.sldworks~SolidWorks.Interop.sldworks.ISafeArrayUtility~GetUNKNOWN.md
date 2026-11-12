---
title: "GetUNKNOWN Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetUNKNOWN"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetUNKNOWN.html"
---

# GetUNKNOWN Method (ISafeArrayUtility)

Gets the specified UNKNOWN object in a Variant SafeArray of UNKNOWN objects.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUNKNOWN( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetUNKNOWN(VariantArray, Index)
```

### C#

```csharp
System.object GetUNKNOWN(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetUNKNOWN(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of UNKNOWN objects
- `Index`: Index of UNKNOWN object

### Return Value

UNKNOWN object

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutUNKNOWN Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutUNKNOWN.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
