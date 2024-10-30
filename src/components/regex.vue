<template>
  <div>
    <a-input v-model:value="regexp" placeholder="">
      <template #prefix> / </template>
      <template #suffix> / </template>
    </a-input>
    <a-dropdown>
      <a-button> 修饰符 <DownOutlined /> </a-button>
      <template #overlay>
        <a-checkbox-group v-model:value="modifier" name="checkboxgroup" :options="options" />
      </template>
    </a-dropdown>
    <div class="text">{{text}}</div>
    <p>
      This regex is highlighted inline:
      <code class="regex">(?&lt;=\d)\p{L}\8</code>.

      And here's the same regex but with different rules from flag u:
      <code class="regex" data-flags="u">(?&lt;=\d)\p{L}\8</code>.
    </p>
    <a-textarea v-model:value="text" placeholder="在此输入待匹配文本" allow-clear />

  </div>
</template>>
<script lang="ts">
import { defineComponent } from 'vue'
import { DownOutlined } from '@ant-design/icons-vue';
import { colorizeAll } from 'regex-colorizer';
export default defineComponent({
  data () {
    return {
      regexp: '',
      modifier: [],
      text: '123456789abcdefghijklmnopqrstuvwxyz中文内容',
      options: [
        { label: '全局搜索', value: 'g' },
        { label: '忽略大小写', value: 'i' },
        { label: '多行模式', value: 'm' },
        { label: '包含换行符', value: 's' },
      ]
    }
  },
  watch: {
    text () {
      colorizeAll({ selector: '.text' })
    }
  },
  mounted () {
    /**
     * 1.https://www.jyshare.com/front-end/854/
     * 2.https://www.regexp.cn/Regex
     * 3.https://slevithan.github.io/regex-colorizer/demo/
     * */ 
    // const str = colorizePattern('(?<=\\d)', {
    //     flags: 'u',
    //   });
    colorizeAll()
  },
  components: {
    DownOutlined
  }
})
</script>