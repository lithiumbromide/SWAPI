---
title: "LoadLineStyle Method (ILineStyleManager)"
project: ""
interface: "ILineStyleManager"
member: "LoadLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~LoadLineStyle.html"
---

# LoadLineStyle Method (ILineStyleManager)

Loads and gets the specified simple LineStyle.

## Syntax

### Visual Basic

```vb
Function LoadLineStyle( _
   ByVal Name As System.String, _
   ByVal FileName As System.String, _
   ByRef LineStyle As LineStyle _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e LoadLineStyle(
   System.string Name,
   System.string FileName,
   out LineStyle LineStyle
)
```

### JScript

```
function LoadLineStyle(
   Name : System.String,
   FileName : System.String,
   LineStyle : LineStyle
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e LoadLineStyle(
   System.string* Name,
   System.string* FileName,
   [PARAMFLAG::Out] LineStyle* LineStyle
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e LoadLineStyle(
   System.String^ Name,
   System.String^ FileName,
   [Out] LineStyle^ LineStyle
)
```

### Parameters

- `Name`: Name of the simple LineStyle to load in the document
- `FileName`: Path and file name of the definition file (see **Remarks**)
- `LineStyle`: Simple [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)

### Return Value

Result as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Load and Activate LineStyles (C#)](Load_and_Activate_LineStyles_Example_CSharp.htm)
[Load and Activate LineStyles (VB.NET)](Laod_and_Activate_LineStyles_Example_VBNET.htm)
[Load and Activate LineStyles (VBA)](Load_and_Activate_LineStyles_Example_VBA.htm)
[Load and Activate LineStyles (JavaScript)](Load_and_Activate_LineStyles_Example_JS.htm)

## Remarks

You must [create simple LineStyles](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateLineStyle.html) before you can load them.

Definition files for simple LineStyles are stored in ASCII text files with **.lin** filename extensions.

If the specified simple LineStyle already exists in the document, then it is not overwritten.

## See Also

[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ILineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager_members.html)
[ILineStyleManager::GetActiveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetActiveLineStyle.html)
[ILineStyleManager::GetLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyle.html)
[ILineStyleManager::GetLineStyles Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~GetLineStyles.html)
[ILineStyleManager::RemoveLineStyle Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~RemoveLineStyle.html)

## Availability

DraftSight V1R4.0
