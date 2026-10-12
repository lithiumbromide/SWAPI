---
title: "Suppression Property (IEquationMgr)"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr"
member: "Suppression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~Suppression.html"
---

# Suppression Property (IEquationMgr)

Obsolete as of SOLIDWORKS 2014 and later.

## Syntax

### Visual Basic (Declaration)

```vb
Property Suppression( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEquationMgr
Dim Index As System.Integer
Dim value As System.Boolean

instance.Suppression(Index) = value

value = instance.Suppression(Index)
```

### C#

```csharp
System.bool Suppression(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.bool Suppression {
   System.bool get(System.int Index);
   void set (System.int Index, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the equation

### Property Value

True if the equation is suppressed, false if not

## VBA Syntax

See [EquationMgr::Suppression](ms-its:sldworksapivb6.chm::/sldworks~EquationMgr~Suppression.html).

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html)

## Availability

SOLIDWORKS 2001Plus, Revision Number 10.0
