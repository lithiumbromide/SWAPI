---
title: "ForceUpdateElectricalData2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ForceUpdateElectricalData2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ForceUpdateElectricalData2.html"
---

# ForceUpdateElectricalData2 Method (IAssemblyDoc)

Forces an update of electrical data.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceUpdateElectricalData2( _
   ByVal Stream As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Stream As System.Integer
Dim value As System.Integer

value = instance.ForceUpdateElectricalData2(Stream)
```

### C#

```csharp
System.int ForceUpdateElectricalData2(
   System.int Stream
)
```

### C++/CLI

```cpp
System.int ForceUpdateElectricalData2(
   System.int Stream
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Stream`: Stream as defined in swElectricalStreamType_e

### Return Value

Status of update as defined in swForceUpdateElectricalDataError_e

## VBA Syntax

See [AssemblyDoc::ForceUpdateElectricalData2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ForceUpdateElectricalData2.html).

## Remarks

Third-party applications should use this method to tell the SOLIDWORKS Design software that they have changed the electrical data. The SOLIDWORKS Design software then re-reads the data to get the updates.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
