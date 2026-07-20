---
title: "CreateMateData Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CreateMateData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMateData.html"
---

# CreateMateData Method (IAssemblyDoc)

Creates a mate feature data object for the specified mate type.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMateData( _
   ByVal Type As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Type As System.Integer
Dim value As System.Object

value = instance.CreateMateData(Type)
```

### C#

```csharp
System.object CreateMateData(
   System.int Type
)
```

### C++/CLI

```cpp
System.Object^ CreateMateData(
   System.int Type
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Type`: Type of mate to create as defined in

[swMateType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html)

(see

Remarks

)

### Return Value

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html)

## VBA Syntax

See

[AssemblyDoc::CreateMateData](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CreateMateData.html)

.

## Examples

See

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html)

examples.

## Remarks

Type must be one of the following mate types as defined in swMateType_e:

- swMateANGLE
- swMateCAMFOLLOWER
- swMateCOINCIDENT
- swMateCONCENTRIC
- swMateDISTANCE
- swMateGEAR
- swMateHINGE
- swMateLINEARCOUPLER
- swMateLOCK
- swMatePARALLEL
- swMatePERPENDICULAR
- swMatePROFILECENTER
- swMateRACKPINION
- swMateSCREW
- swMateSLOT
- swMateSYMMETRIC
- swMateTANGENT
- swMateUNIVERSALJOINT
- swMateWIDTH

To create a mate, see the[IAssemblydoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html)Remarks section.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

[IAssemblyDoc::AutoMateRepair Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
