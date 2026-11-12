---
title: "GetUserUnit Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit.html"
---

# GetUserUnit Method (ISldWorks)

Gets an empty [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) object of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUserUnit( _
   ByVal UnitType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UnitType As System.Integer
Dim value As System.Object

value = instance.GetUserUnit(UnitType)
```

### C#

```csharp
System.object GetUserUnit(
   System.int UnitType
)
```

### C++/CLI

```cpp
System.Object^ GetUserUnit(
   System.int UnitType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitType`: Unit type as defined in [swUserUnitsType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

### Return Value

IUserUnit

## VBA Syntax

See [SldWorks::GetUserUnit](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetUserUnit.html).

## Remarks

The instance of IUserUnit returned by this method is read-write, not persistent, and not tied to any document. Use this instance as a template to store units properties at runtime.

Call [IModelDoc2::GetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html) to get the user units of a document.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserUnit.html)
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
