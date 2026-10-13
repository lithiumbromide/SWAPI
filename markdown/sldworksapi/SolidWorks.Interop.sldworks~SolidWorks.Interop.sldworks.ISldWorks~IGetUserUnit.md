---
title: "IGetUserUnit Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetUserUnit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserUnit.html"
---

# IGetUserUnit Method (ISldWorks)

Gets an empty [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html) object of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserUnit( _
   ByVal UnitType As System.Integer _
) As UserUnit
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim UnitType As System.Integer
Dim value As UserUnit

value = instance.IGetUserUnit(UnitType)
```

### C#

```csharp
UserUnit IGetUserUnit(
   System.int UnitType
)
```

### C++/CLI

```cpp
UserUnit^ IGetUserUnit(
   System.int UnitType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UnitType`: Unit type as defined in [swUserUnitsType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

### Return Value

IUserUnit

## VBA Syntax

See [SldWorks::IGetUserUnit](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetUserUnit.html).

## Remarks

The instance of IUserUnit returned by this method is read-write, not persistent, and not tied to any document. Use this instance as a template to store units properties at runtime.

Call [IModelDoc2::IGetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.html) to get the user units of a document.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit.html)
[IModelDoc2::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
