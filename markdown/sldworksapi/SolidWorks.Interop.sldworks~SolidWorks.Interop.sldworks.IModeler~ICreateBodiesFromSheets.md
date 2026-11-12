---
title: "ICreateBodiesFromSheets Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodiesFromSheets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets.html"
---

# ICreateBodiesFromSheets Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodiesFromSheets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodiesFromSheets( _
   ByVal NSheets As System.Integer, _
   ByRef Sheets As System.Object, _
   ByVal Options As System.Integer, _
   ByRef NResults As System.Integer, _
   ByRef Results As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NSheets As System.Integer
Dim Sheets As System.Object
Dim Options As System.Integer
Dim NResults As System.Integer
Dim Results As System.Object
Dim value As System.Integer

value = instance.ICreateBodiesFromSheets(NSheets, Sheets, Options, NResults, Results)
```

### C#

```csharp
System.int ICreateBodiesFromSheets(
   System.int NSheets,
   ref System.object Sheets,
   System.int Options,
   out System.int NResults,
   out System.object Results
)
```

### C++/CLI

```cpp
System.int ICreateBodiesFromSheets(
   System.int NSheets,
   System.Object^% Sheets,
   System.int Options,
   [Out] System.int NResults,
   [Out] System.Object^ Results
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NSheets`:
- `Sheets`:
- `Options`:
- `NResults`:
- `Results`:

## VBA Syntax

See [Modeler::ICreateBodiesFromSheets](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodiesFromSheets.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
