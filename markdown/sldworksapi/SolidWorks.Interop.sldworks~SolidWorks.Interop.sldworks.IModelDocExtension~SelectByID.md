---
title: "SelectByID Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SelectByID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID.html"
---

# SelectByID Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByID( _
   ByVal Name As System.String, _
   ByVal Type As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Append As System.Boolean, _
   ByVal Mark As System.Integer, _
   ByVal Callout As Callout _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim Type As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Append As System.Boolean
Dim Mark As System.Integer
Dim Callout As Callout
Dim value As System.Boolean

value = instance.SelectByID(Name, Type, X, Y, Z, Append, Mark, Callout)
```

### C#

```csharp
System.bool SelectByID(
   System.string Name,
   System.string Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout Callout
)
```

### C++/CLI

```cpp
System.bool SelectByID(
   System.String^ Name,
   System.String^ Type,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Append,
   System.int Mark,
   Callout^ Callout
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Type`:
- `X`:
- `Y`:
- `Z`:
- `Append`:
- `Mark`:
- `Callout`:

## VBA Syntax

See [ModelDocExtension::SelectByID](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SelectByID.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
