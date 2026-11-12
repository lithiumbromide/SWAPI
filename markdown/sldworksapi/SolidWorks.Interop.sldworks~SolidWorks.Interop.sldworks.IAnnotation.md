---
title: "IAnnotation Interface"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html"
---

# IAnnotation Interface

Allows access to notes, weld symbols, datum tags, display dimensions, blocks, cosmetic threads, center marks, centerlines, and other annotation types.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
```

### C#

```csharp
public interface IAnnotation
```

### C++/CLI

```cpp
public interface class IAnnotation
```

## VBA Syntax

See [Annotation](ms-its:sldworksapivb6.chm::/sldworks~Annotation.html).

## Examples

[Get Whether Note Contains Rich-embedded Text (VBA)](Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)
[Select Table Cells (C#)](Select_Table_Cells_Example_CSharp.htm)
[Select Table Cells (VB.NET)](Select_Table_Cells_Example_VBNET.htm)
[Select Table Cells (VBA)](Select_Table_Cells_Example_VB.htm)

## Remarks

Because IAnnotation is a high-level representation of all annotation types, it provides functions that are generic to all types of annotations. For example, every annotation has a name and position, so IAnnotation provides functions that access this data.

Although IAnnotation has specific lower-level objects (such as [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)), it does not have any derived classes in the SOLIDWORKS API. This means that you cannot use an IAnnotation pointer to call functions in the lower-level objects. You also cannot use QueryInterface to obtain the underlying classes. Instead, SOLIDWORKS provides [IAnnotation::GetSpecificAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.html), which accesses underlying objects.

Similarly if you are holding onto a lower-level class, then you can obtain the corresponding IAnnotation object using the GetAnnotation method of that class (see the **Accessors** list in this topic).

## Accessors

[IAnnotation::GetNext3 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetNext3.html)

[IAnnotationView::Annotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~Annotations.html)

[IAnnotationView::IGetAnnotations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView~IGetAnnotations.html)

[ICenterLine::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2283' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2283'

[ICenterMark::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2326'

[ICenterOfMass::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterOfMass~GetAnnotation.html) and [ICenterOfMass::IGetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterOfMass~IGetAnnotation.html) designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2326'

[ICThread::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~GetAnnotation.html) and [ICThread::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICThread~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3686' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3686'

[IDatumOrigin::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumOrigin~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2328'

[IDatumTag::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetAnnotation.html) and [IDatumTag::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3687' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3687'

[IDatumTargetSym::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetAnnotation.html) and [IDatumTargetSym::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3688'

[IDisplayDimension::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetAnnotation.html) and [IDisplayDimension::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3689' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2331'

[IDowelSymbol::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol~GetAnnotation.html) and [IDowelSymbol::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3690' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3690'

[IGtol::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2337'

[ILayer::GetItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetItems.html)

[IModelDoc2::GetFirstAnnotation2 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetFirstAnnotation2.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2345' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2345'

[IModelDocExtension::GetAnnotations Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAnnotations.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2346' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2346'

[IModelDocExtension::InsertAnnotationFavorite Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertAnnotationFavorite.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2347' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2347'

[IMultiJogLeader::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader~GetAnnotation.html) and [IMultiJogLeader::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMultiJogLeader~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3692' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2348'

[INote::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetAnnotation.html) and [INote::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~IGetAnnotation.html)

[IRevisionCloud::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~GetAnnotation.html) and [IRevisionCloud::IGetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionCloud~IGetAnnotation.html)

[ISFSymbol::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2350' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2350'

[ITableAnnotation::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2351' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2351'

[IView::GetAnnotations Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetAnnotations.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2352' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2352'

[IView::GetFirstAnnotation3 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstAnnotation3.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2353' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2353'

[IWeldBead::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2354' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2354'

[IWeldSymbol::GetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c2355' and [IWeldSymbol::IGetAnnotation Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~IGetAnnotation.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation|c3694'

## Access Diagram

[Annotation](SWObjectModel.pdf#Annotation)

## See Also

[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::GetObjectId Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId.html)
