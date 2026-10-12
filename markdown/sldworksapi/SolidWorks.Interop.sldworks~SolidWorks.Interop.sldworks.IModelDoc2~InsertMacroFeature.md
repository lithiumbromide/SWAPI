---
title: "InsertMacroFeature Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertMacroFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMacroFeature.html"
---

# InsertMacroFeature Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertMacroFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMacroFeature3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMacroFeature( _
   ByVal CmdFile As System.String, _
   ByVal CmdModule As System.String, _
   ByVal CmdProcedure As System.String, _
   ByVal ParamNames As System.Object, _
   ByVal ParamTypes As System.Object, _
   ByVal ParamValues As System.Object, _
   ByVal PmFile As System.String, _
   ByVal PmModule As System.String, _
   ByVal PmProcedure As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CmdFile As System.String
Dim CmdModule As System.String
Dim CmdProcedure As System.String
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object
Dim PmFile As System.String
Dim PmModule As System.String
Dim PmProcedure As System.String
Dim value As System.Object

value = instance.InsertMacroFeature(CmdFile, CmdModule, CmdProcedure, ParamNames, ParamTypes, ParamValues, PmFile, PmModule, PmProcedure)
```

### C#

```csharp
System.object InsertMacroFeature(
   System.string CmdFile,
   System.string CmdModule,
   System.string CmdProcedure,
   System.object ParamNames,
   System.object ParamTypes,
   System.object ParamValues,
   System.string PmFile,
   System.string PmModule,
   System.string PmProcedure
)
```

### C++/CLI

```cpp
System.Object^ InsertMacroFeature(
   System.String^ CmdFile,
   System.String^ CmdModule,
   System.String^ CmdProcedure,
   System.Object^ ParamNames,
   System.Object^ ParamTypes,
   System.Object^ ParamValues,
   System.String^ PmFile,
   System.String^ PmModule,
   System.String^ PmProcedure
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CmdFile`:
- `CmdModule`:
- `CmdProcedure`:
- `ParamNames`:
- `ParamTypes`:
- `ParamValues`:
- `PmFile`:
- `PmModule`:
- `PmProcedure`:

## VBA Syntax

See [ModelDoc2::InsertMacroFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertMacroFeature.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
