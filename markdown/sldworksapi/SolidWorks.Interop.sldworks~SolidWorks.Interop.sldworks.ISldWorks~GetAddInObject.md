---
title: "GetAddInObject Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetAddInObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject.html"
---

# GetAddInObject Method (ISldWorks)

Gets an add-in object for the specified SOLIDWORKS add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAddInObject( _
   ByVal Clsid As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Clsid As System.String
Dim value As System.Object

value = instance.GetAddInObject(Clsid)
```

### C#

```csharp
System.object GetAddInObject(
   System.string Clsid
)
```

### C++/CLI

```cpp
System.Object^ GetAddInObject(
   System.String^ Clsid
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Clsid`: GUID or ProgID of the add-in as registered with SOLIDWORKS (see Remarks)

### Return Value

Your add-in object

## VBA Syntax

See [SldWorks::GetAddInObject](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetAddInObject.html).

## Remarks

To specify Clsid with:

- a ProgID, read [Accessing SOLIDWORKS Add-in Objects](sldworksapiprogguide.chm::/Overview/Accessing_Add-ins.htm).
- a GUID, use curly brackets as in "{`GUID`}", or the string is interpreted as a ProgID.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::LoadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html)
[ISldWorks::UnloadAddIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnloadAddIn.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
