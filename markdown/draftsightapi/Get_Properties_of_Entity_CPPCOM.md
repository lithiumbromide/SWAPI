---
title: "Get Properties of Entity Example (COM native C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Get_Properties_of_Entity_CPPCOM.htm"
---

# Get Properties of Entity Example (COM native C++)

class CAddinDumpManager
{
public:

template<class EntityTypePtr>
static void DumpGraphicsEntity(EntityTypePtr entity, CStdioFile& fo )
{
CString strPrint;
**bstr_t LayerName = entity->GetLayer();**
strPrint.Format(L"\tLayer: s\r\n", LayerName.operator const wchar_t*());
fo.WriteString(strPrint);

**_bstr_t LineType = entity->GetLineStyle();**
strPrint.Format(L"\tLineStyles\r\n", LineStyle.operator const wchar_t*());
fo.WriteString(strPrint);

**double** **LinetypeScale = entity->GetLineScale( );**
strPrint.Format(L"\tLineScale: .4f\r\n", LineScale);
fo.WriteString(strPrint);

**dsLineWeight_e LineWeight = entity->GetLineWeight();**
if( dsLnWt_ByLayer == LineWeight )
strPrint.Format(L"\tLineWeight: ByLayer\r\n");
else
if( dsLnWt_ByBlock == LineWeight )
strPrint.Format(L"\tLineWeight: ByBlock\r\n");
else
if( dsLnWt_ByLwDefault == LineWeight )
strPrint.Format(L"\tLineWeight: ByLwDefault\r\n");
else
strPrint.Format(L"\tLineWeightd\r\n", (int)LineWeight);
fo.WriteString(strPrint);

**VARIANT_BOOL isVisible = entity->GetVisible();**
if(VARIANT_TRUE == isVisible)
strPrint.Format(L"\tVisible: true\r\n");
else
strPrint.Format(L"\tVisible: false\r\n");
fo.WriteString(strPrint);
};

};
