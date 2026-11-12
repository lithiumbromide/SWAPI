---
title: "CreateBodiesFromSheets Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateBodiesFromSheets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets.html"
---

# CreateBodiesFromSheets Method (IModeler)

Obsolete. Superseded by [IModeler::CreateBodiesFromSheets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBodiesFromSheets( _
   ByVal Sheets As System.Object, _
   ByVal Options As System.Integer, _
   ByRef Error As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Sheets As System.Object
Dim Options As System.Integer
Dim Error As System.Integer
Dim value As System.Object

value = instance.CreateBodiesFromSheets(Sheets, Options, Error)
```

### C#

```csharp
System.object CreateBodiesFromSheets(
   System.object Sheets,
   System.int Options,
   out System.int Error
)
```

### C++/CLI

```cpp
System.Object^ CreateBodiesFromSheets(
   System.Object^ Sheets,
   System.int Options,
   [Out] System.int Error
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Sheets`:
- `Options`:
- `Error`:

## VBA Syntax

See [Modeler::CreateBodiesFromSheets](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateBodiesFromSheets.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
